记得构建：

```jsonc
// .vscode/tasks.json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Bolt Build",
            "type": "shell",
            "command": "beet",
            "args": [
                "build",
                "-l",
                "path/to/ACLCCGalgame-Minecraft-Edition"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "options": {
                "cwd": "path/to/ACLCCGalgame-Minecraft-Edition/beet"
            }
        }
    ]
}
```

当你用VSCode打开世界文件夹时，一种可行的配置

```jsonc
// .vscode/tasks.json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Bolt Build",
            "type": "shell",
            "command": "beet",
            "args": [
                "build",
                "-l",
                ".."
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "options": {
                "cwd": "beet"
            }
        }
    ]
}
```