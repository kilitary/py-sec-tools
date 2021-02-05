rule _ACProtect_V1_3X__risco_hxbyat
{
	meta:
		description = "ACProtect V1_3X __ risco"
	strings:
		$a = {601EE83B01BFCC012E033ECA012EC705}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
