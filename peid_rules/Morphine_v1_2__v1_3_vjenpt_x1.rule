rule _Morphine_v1_2__v1_3_vjenpt
{
	meta:
		description = "Morphine v1_2 _ v1_3"
	strings:
		$a = {FF2534??5A008BC0FF2538??5A008BC0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
