rule _CAN_Crunched_ANsi_file_udpyyl
{
	meta:
		description = "CAN _Crunched ANsi_ file"
	strings:
		$a = {CA01}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
