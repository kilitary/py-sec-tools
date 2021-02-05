rule _PROTECT_EXECOM_v5_0_glnoka
{
	meta:
		description = "PROTECT_ EXECOM v5_0"
	strings:
		$a = {1E0E0E1F07}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
