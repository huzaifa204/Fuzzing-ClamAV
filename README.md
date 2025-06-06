# Fuzzing-ClamAV
Experimenting on the ClamAV antivirus, by fuzzing it through various methods.

Phase 1: This involved setting up the environment for fuzzing ClamAV. I have used Kali Linux installed on Oracle VirtualBox.
         Python3 version: 3.13.3
         Clang used( GCC has known errors when installing "FuzzingBook" library, error likely arises due to version 
         incompatibility.

Phase 2: Implements blackbox testing by generating random input files to evaluate system robustness, accompanied by automated            scanning using ClamAV for vulnerability detection. Original ClamAV scan takes a lot of time, preferably use ClamAV              daemon which promises faster execution times.
