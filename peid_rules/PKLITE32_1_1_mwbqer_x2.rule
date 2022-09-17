rule _PKLITE32_1_1_mwbqer
{
	meta:
		description = "PKLITE32 1_1"
	strings:
		$a = {504B4C495445333220436F707972696768742031}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
