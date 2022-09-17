rule _PECompact_v2_0_ykcinv
{
	meta:
		description = "PECompact v2_0"
	strings:
		$a = {B8????????5064FF35000000006489250000000033C089085045436F6D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
