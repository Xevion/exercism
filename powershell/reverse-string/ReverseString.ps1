Function Get-ReverseString {
    [CmdletBinding()]
    Param(
        [Parameter(Position=1, ValueFromPipeline=$true)]
        [string]$Forward
	)
	
    $x = $Forward.ToCharArray()
    [array]::Reverse($x)
    return -join $x
}
