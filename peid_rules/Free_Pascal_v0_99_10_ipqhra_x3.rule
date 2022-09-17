rule _Free_Pascal_v0_99_10_ipqhra
{
	meta:
		description = "Free Pascal v0_99_10"
	strings:
		$a = {C605????4000??E8????0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
