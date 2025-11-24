#!/usr/bin/env nu

def --wrapped main [...rest] {
  const pathToSelf = path self
  let nameOfSelf = $pathToSelf | path parse | get stem
  if $rest in [ [-h] [--help] ] {
    ^$nu.current-exe -c $'use ($pathToSelf); scope modules | where name == ($nameOfSelf) | get 0.commands.name'
  } else {
    ^$nu.current-exe -c $'use ($pathToSelf); ($nameOfSelf) ($rest | str join (" "))'
  }
}

export def download-challenge [problemNumber] {
  const path_to_src_folder = [(path self) .. project_euler] | path join
  let file = http get $"https://projecteuler.net/problem=($problemNumber)"
  | parse '<title>#{number} {title} - Project Euler</title>'
  | get title.0
  | str snake-case
  | {
    parent: $path_to_src_folder
    stem: $"test_pe($problemNumber)_($in)"
    extension: py
  }
  | path join
  http get $"https://projecteuler.net/minimal=($problemNumber)"
  | lines
  | each { $"# ($in)" }
  | prepend $"# <https://projecteuler.net/problem=($problemNumber)>"
  | append [ $"# Notes:" "#  " ]
  | str join (char newline)
  | save $file
}

export def update-readme [] {
$"
<div align=\"center\">
  <img src=\"https://projecteuler.net/profile/NonlinearFruit.png\"/>
  <img src=\"https://projecteuler.net/profile/unclebobmartin.png\"/>
  <img src=\"https://projecteuler.net/profile/africh.png\"/>
</div>

# [Project Euler]\(https://projecteuler.net)

## Solutions

(table-of-scores)

## How To

- [required] pdm <https://github.com/pdm-project/pdm>
- [required] `pdm install`
```sh
./toolkit.nu download-challenge $CHALLENGE
git add -A
vim project_euler/ # Edit challenge
pdm test           # Run tests
./toolkit.nu update-readme
git add -A
git commit -m \"Solve PE $CHALLENGE: $TITLE\"
```

## Help

(help-docs)
"
  | save -f README.md
}

def table-of-scores [] {
  ls project_euler/test_*
  | each {|file|
    $file.name
    | path parse
    | get stem
    | parse "test_pe{number}_{challenge}"
    | first
    | update number { into int }
    | update challenge { str title-case }
    | insert links {|it|
      $"\([src]\(($file.name))) \([web]\(https://projecteuler.net/problem=($it.number)))"
    }
  }
  | sort-by number
  | to md
}

def help-docs [] {
  scope modules
  | where name == toolkit
  | get commands.0.name
  | each {|cmd|
    ^nu -c $"use toolkit.nu; toolkit ($cmd) -h"
    | str trim
    | $"
<details><summary>toolkit ($cmd)</summary>

```
($in)
```
</details>
    "
  }
  | to text
  | ansi strip
}
