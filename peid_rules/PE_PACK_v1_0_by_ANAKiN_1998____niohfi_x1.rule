rule _PE_PACK_v1_0_by_ANAKiN_1998____niohfi
{
	meta:
		description = "PE_PACK v1_0 by ANAKiN 1998 _____"
	strings:
		$a = {74??E9????????00000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
