rule _NsPacK_Net__LiuXingPing_wpucjt
{
	meta:
		description = "NsPacK _Net __ LiuXingPing"
	strings:
		$a = {5669727475616C50726F746563740000BB0147657453797374656D496E666F004B45524E454C33322E646C6C00005E005F436F72??????4D61696E006D73636F7265652E646C6C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
