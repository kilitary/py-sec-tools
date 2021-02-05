rule _aPack_v0_82_iehrjf
{
	meta:
		description = "aPack v0_82"
	strings:
		$a = {1E068CCBBA????03DA8D??????FC33F633FF484B8EC08EDB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
