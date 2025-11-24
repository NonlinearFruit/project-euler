
<div align="center">
  <img src="https://projecteuler.net/profile/NonlinearFruit.png"/>
  <img src="https://projecteuler.net/profile/unclebobmartin.png"/>
  <img src="https://projecteuler.net/profile/africh.png"/>
</div>

# [Project Euler](https://projecteuler.net)

## Solutions

| number | challenge | links |
| --- | --- | --- |
| 88 | Product Sum Numbers | ([src](project_euler/test_pe88_product_sum_numbers.py)) ([web](https://projecteuler.net/problem=88)) |
| 700 | Eulercoin | ([src](project_euler/test_pe700_eulercoin.py)) ([web](https://projecteuler.net/problem=700)) |
| 800 | Hybrid Integers | ([src](project_euler/test_pe800_hybrid_integers.py)) ([web](https://projecteuler.net/problem=800)) |
| 816 | Shortest Distance Among Points | ([src](project_euler/test_pe816_shortest_distance_among_points.py)) ([web](https://projecteuler.net/problem=816)) |
| 932 | 2025 | ([src](project_euler/test_pe932_2025.py)) ([web](https://projecteuler.net/problem=932)) |

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
git commit -m "Solve PE $CHALLENGE: $TITLE"
```

## Help


<details><summary>toolkit download-challenge</summary>

```
Usage:
  > download-challenge <problemNumber> 

Flags:
  -h, --help: Display the help message for this command

Parameters:
  problemNumber <any>

Input/output types:
  ╭───┬───────┬────────╮
  │ # │ input │ output │
  ├───┼───────┼────────┤
  │ 0 │ any   │ any    │
  ╰───┴───────┴────────╯
```
</details>
    

<details><summary>toolkit update-readme</summary>

```
Usage:
  > update-readme 

Flags:
  -h, --help: Display the help message for this command

Input/output types:
  ╭───┬───────┬────────╮
  │ # │ input │ output │
  ├───┼───────┼────────┤
  │ 0 │ any   │ any    │
  ╰───┴───────┴────────╯
```
</details>
    

