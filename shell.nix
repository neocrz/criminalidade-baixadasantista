{ pkgs ? import <nixpkgs> { }}:

with pkgs;

let
  myEnv = python311.withPackages (ps: with ps; [
    pandas
    sqlalchemy
  ]);
in
mkShell {
  buildInputs = [ myEnv ];
}
