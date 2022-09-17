rule _ACProtect_V1_4X__risco_axwwoe
{
	meta:
		description = "ACProtect V1_4X __ risco"
	strings:
		$a = {60E8010000006358E8010000007A582D0D1040008D90C110400052508D80491040005D508D85651040005064FF350000000064892500000000CC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
