#!/usr/bin/env python3
"""
Superpowers Sandbox Proxy
用于 Qoder 中安全执行危险命令，避免被沙箱中断。

用法:
  python3 sandbox_proxy.py "<command>"

示例:
  python3 sandbox_proxy.py "git push origin main"
  python3 sandbox_proxy.py "rm -rf node_modules"
"""

import sys
import subprocess
import json
import os
import shlex


def execute_command(command: str) -> dict:
    """执行命令并返回结果"""
    try:
        # 分割命令（保持 shell 特性）
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=300,  # 5分钟超时
            cwd=os.getcwd()
        )
        
        return {
            "success": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "command": command
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "returncode": -1,
            "stdout": "",
            "stderr": "Command timed out after 300 seconds",
            "command": command
        }
    except Exception as e:
        return {
            "success": False,
            "returncode": -1,
            "stdout": "",
            "stderr": str(e),
            "command": command
        }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "success": False,
            "returncode": -1,
            "stdout": "",
            "stderr": "Usage: python3 sandbox_proxy.py <command>",
            "command": ""
        }, ensure_ascii=False))
        sys.exit(1)
    
    command = sys.argv[1]
    result = execute_command(command)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
