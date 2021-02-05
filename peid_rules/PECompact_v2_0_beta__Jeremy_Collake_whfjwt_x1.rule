rule _PECompact_v2_0_beta__Jeremy_Collake_whfjwt
{
	meta:
		description = "PECompact v2_0 beta __ Jeremy Collake"
	strings:
		$a = {B8??????015064FF35000000006489250000000033C089085045436F6D706163743200}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
