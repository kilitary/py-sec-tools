rule _Name_of_the_Packer_v1_0_owwzkk
{
	meta:
		description = "Name of the Packer v1_0"
	strings:
		$a = {50E8????????5825??F0FFFF8BC883C1605183C04083EA0652FF209DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
