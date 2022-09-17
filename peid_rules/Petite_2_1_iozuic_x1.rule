rule _Petite_2_1_iozuic
{
	meta:
		description = "Petite 2_1"
	strings:
		$a = {64FF350000000064892500000000669C60508BD8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
