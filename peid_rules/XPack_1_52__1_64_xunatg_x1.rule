rule _XPack_1_52__1_64_xunatg
{
	meta:
		description = "XPack 1_52 _ 1_64"
	strings:
		$a = {8BECFA33C08ED0BC????2E????????2E????????EB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
