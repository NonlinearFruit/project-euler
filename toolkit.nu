def --wrapped main [...rest] {
  nu -c $'use toolkit.nu; toolkit ($rest | str join (char space))'
}

export def pull [problemNumber] {
  let file = {
    parent: project_euler
    stem: $"test_pe($problemNumber)"
    extension: py
  } | path join
  http get $"https://projecteuler.net/minimal=($problemNumber)"
  | lines
  | each { $"# ($in)" }
  | prepend $"# <https://projecteuler.net/problem=($problemNumber)>"
  | append [ $"# Notes:" "#  " ]
  | str join (char newline)
  | save $file
}
