rule _MSLRH_v0_1__emadicius_ntjfsz
{
	meta:
		description = "MSLRH v0_1 __ emadicius"
	strings:
		$a = {547572626F??50726F66696C6572??6172656173??66696C65}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
