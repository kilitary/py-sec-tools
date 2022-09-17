rule _FIZ_Archive_hhvdpv
{
	meta:
		description = "FIZ Archive"
	strings:
		$a = {46495A1A01}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
