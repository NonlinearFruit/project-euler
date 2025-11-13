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
