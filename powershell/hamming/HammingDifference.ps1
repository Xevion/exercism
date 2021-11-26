function Get-HammingDifference([string]$A, [string]$B) {
    if ($A.Length -ne $B.Length) {
        Throw("Left and right strands must be of equal length.")
    }

    [int] $hamming = 0
    0..$A.Length | % { if ($A[$_] -ne $B[$_]) { $hamming++ } }

    return $hamming
}
