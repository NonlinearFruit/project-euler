#!/usr/bin/env nu

def --wrapped main [...rest] {
  nu -c $'use toolkit.nu; toolkit ($rest | str join (char space))'
}

export def pull [problemNumber] {
  let file = http get $"https://projecteuler.net/problem=($problemNumber)"
  | parse '<title>#{number} {title} - Project Euler</title>'
  | get title.0
  | str snake-case
  | {
    parent: project_euler
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
