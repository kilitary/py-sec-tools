rule _mkfpack__llydd_lideoj
{
	meta:
		description = "mkfpack __ llydd"
	strings:
		$a = {E8000000005B81EB050000008B939F080000536A406800100000526A00FF93320800005B8BF08BBB9B08000003FB5657E88608000083C4088D93BB0800005253FFE6}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
