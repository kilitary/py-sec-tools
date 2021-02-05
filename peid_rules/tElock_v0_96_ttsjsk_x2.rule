rule _tElock_v0_96_ttsjsk
{
	meta:
		description = "tElock v0_96"
	strings:
		$a = {E95300FFFDFFFBFFF9FFBC03008BE54C4CC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
