rule _PECompact_2_x__Jeremy_Collake_umoqwv
{
	meta:
		description = "PECompact 2_x __ Jeremy Collake"
	strings:
		$a = {B8????????5064FF35000000006489250000000033C08908504543}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
