rule _ASProtect_2_0_onyptw
{
	meta:
		description = "ASProtect 2_0"
	strings:
		$a = {6801??4000E801000000C3C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
