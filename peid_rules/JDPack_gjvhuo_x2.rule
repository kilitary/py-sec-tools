rule _JDPack_gjvhuo
{
	meta:
		description = "JDPack"
	strings:
		$a = {60E8????????5D83ED0680BDE004????010F84F2}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
