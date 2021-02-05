rule _Ionic_Wind_Software_mpsebn
{
	meta:
		description = "Ionic Wind Software"
	strings:
		$a = {9BDBE39BDBE2D92D00????005589E5E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
