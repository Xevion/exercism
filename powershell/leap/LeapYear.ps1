function Test-LeapYear {
    param( [int]$year )

    if ((($year % 4 -eq 0) -and !($year % 100 -eq 0)) -or ($year % 400 -eq 0)) {
        return $true
    }
    
    return $false
}
