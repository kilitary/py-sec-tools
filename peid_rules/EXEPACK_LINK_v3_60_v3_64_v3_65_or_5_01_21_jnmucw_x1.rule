rule _EXEPACK_LINK_v3_60_v3_64_v3_65_or_5_01_21_jnmucw
{
	meta:
		description = "EXEPACK _LINK_ v3_60_ v3_64_ v3_65 or 5_01_21"
	strings:
		$a = {8CC005????0E1FA3????03??????8EC08B??????8B??4F8BF7FDF3A450B8????50CB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
