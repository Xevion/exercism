Function Get-BobResponse() {
    <#
    .SYNOPSIS
    Bob is a lackadaisical teenager. In conversation, his responses are very limited.
    
    .DESCRIPTION
    Bob is a lackadaisical teenager. In conversation, his responses are very limited.

    Bob answers 'Sure.' if you ask him a question.

    He answers 'Whoa, chill out!' if you yell at him.

    He answers 'Calm down, I know what I'm doing!' if you yell a question at him.

    He says 'Fine. Be that way!' if you address him without actually saying
    anything.

    He answers 'Whatever.' to anything else.
    
    .PARAMETER HeyBob
    The sentence you say to Bob.
    
    .EXAMPLE
    Get-BobResponse -HeyBob "Hi Bob"
    #>
    [CmdletBinding()]
    Param(
        [string]$HeyBob
    )

    # Not a single lowercase letter in the entire string
    if (($HeyBob -cnotmatch '[a-z]') -and ($HeyBob -match '[A-Z]')) {
        if ($HeyBob -match '\?$') {
            return 'Calm down, I know what I''m doing!'
        } else {
            return 'Whoa, chill out!'
        }
    }

    # Ends with question mark
    if ($HeyBob -match '\?\s*$') { return 'Sure.' }

    # 0 or more whitespace characters from start to end
    if ($HeyBob -match '^\s*$') { return 'Fine. Be that way!'}

    return 'Whatever.'
}
