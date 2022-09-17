rule _aPack_v0_98b_DS__ES_not_saved__ukuhry
{
	meta:
		description = "aPack v0_98b _DS _ ES not saved_"
	strings:
		$a = {8CCBBA????03DAFC33F633FF4B8EDB8D??????8EC0B9????F3A54A75}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
