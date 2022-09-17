rule _PECompact_v2_0_ujuukn
{
	meta:
		description = "PECompact v2_0"
	strings:
		$a = {B8????????05????????5064FF350000000064892500000000CC90909090}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
