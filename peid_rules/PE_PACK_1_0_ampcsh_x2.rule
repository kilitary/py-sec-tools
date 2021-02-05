rule _PE_PACK_1_0_ampcsh
{
	meta:
		description = "PE_PACK 1_0"
	strings:
		$a = {50FCAD33C2AB8BD0E2F8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
