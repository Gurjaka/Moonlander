let 
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  packages = [
    pkgs.python3
    pkgs.zsh
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.matplotlib
      python-pkgs.numpy
    ]))
  ];
  shellHook = ''
    echo "Welcome to Moonlander development shell!"
    exec zsh
  '';
} 
