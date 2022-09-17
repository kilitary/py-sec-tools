rule _PECompact_2_0x_Heuristic_Mode__Jeremy_Collake_xgepqz
{
	meta:
		description = "PECompact 2_0x Heuristic Mode __ Jeremy Collake"
	strings:
		$a = {B8??????005064FF35000000006489250000000033C089085045436F6D706163743200}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
