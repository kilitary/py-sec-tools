rule _ACProtect_V1_3X__risco_mvzmcw
{
	meta:
		description = "ACProtect V1_3X __ risco"
	strings:
		$a = {6050E8010000007583}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
