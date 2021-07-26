let
  mach-nix = import
    (builtins.fetchGit {
      url = "https://github.com/DavHau/mach-nix/";
      ref = "refs/tags/3.2.0";
    })
    {
      python = "python38";
    };
in
mach-nix.mkPythonShell {
  requirements = builtins.readFile ./requirements.txt;
}
