# Benchmark

This repository contains code and data used to benchmark different pull request review tools.

## Overview

The goal of this benchmark is to simulate realistic scenarios where buggy code is submitted via pull requests. Each test case consists of a buggy version of a repository and a corresponding fixed version. By submitting a pull request from the buggy version to the fixed version, we can evaluate how effectively a review tool detects issues.

## Repository Structure

- Each folder in the `main` branch represents a **fixed version** of a repository where a specific issue has already been resolved.
- Folder names follow the format: `reponame_id`, where:
  - `reponame` is the name of the repository.
  - `id` is a unique identifier for the test case.

- For each fixed version, there is a corresponding **buggy version** located in a branch named: `test_<reponame_id>`

## How It Works

1. The `main` branch contains the fixed versions of all test repositories.
2. The `test_<reponame_id>` branches contain the buggy versions of the same repositories.
3. To create a benchmark scenario:
   - Create a pull request from the `test_<reponame_id>` branch to the `main` branch.
   - This simulates a developer submitting a buggy pull request.
4. Run your pull request review tool on the simulated PR to evaluate its performance.

## Example

Given a folder `shoppingcart_01` in the `main` branch:
- The fixed version of the `shoppingcart` repo is in `main/shoppingcart_01`.
- The buggy version is in the branch `test_shoppingcart_01`.
- You create a pull request from `test_shoppingcart_01` to `main`, targeting the `shoppingcart_01` folder.

## Current Dataset

The current benchmark uses real-world issues extracted from the [`maniple`](https://github.com/PyRepair/maniple) dataset. Specifically, it focuses on bugs found in the [`tqdm`](https://github.com/tqdm/tqdm) project.

## Test Cases: `tqdm`

Each test case below corresponds to a buggy-to-fixed repository pair.

### Tqdm Issues
- tqdm_1
  - Related issues:
     - https://github.com/tqdm/tqdm/issues/402
     - https://github.com/tqdm/tqdm/issues/840
     - https://github.com/tqdm/tqdm/issues/480
- tqdm_3
  - Related issues:
     - https://github.com/tqdm/tqdm/issues/353
- tqdm_4
  - Related issues:
     - Not available
- tqdm_5
  - Related issues:
     - https://github.com/tqdm/tqdm/issues/574
- tqdm_6
  - Related issues:
     - https://github.com/tqdm/tqdm/issues/539
- tqdm_8
  - Related issues:
     - Not available

### Thefuck Issues
- thefuck_1
  - Related issues:
     - https://github.com/nvbn/thefuck/issues/1047
- thefuck_2
  - Related issues:
     - Not available
- thefuck_3
  - Related issues:
     - https://github.com/nvbn/thefuck/issues/869