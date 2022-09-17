rule _SuckStop_v1_11_uhllht
{
	meta:
		description = "SuckStop v1_11"
	strings:
		$a = {EB??????BE????B430CD21EB??9B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
