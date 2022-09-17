rule _tElock_v0_70_uxxvgv
{
	meta:
		description = "tElock v0_70"
	strings:
		$a = {60E8BD100000C383E200F975FA70}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
