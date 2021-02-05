rule _SafeDisc_v4_zigtmo
{
	meta:
		description = "SafeDisc v4"
	strings:
		$a = {000000000000000000000000426F475F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
