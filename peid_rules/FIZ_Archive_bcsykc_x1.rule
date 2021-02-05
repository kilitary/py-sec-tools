rule _FIZ_Archive_bcsykc
{
	meta:
		description = "FIZ Archive"
	strings:
		$a = {46495A1A01}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
