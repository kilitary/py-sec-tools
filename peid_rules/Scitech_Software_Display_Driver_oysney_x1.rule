rule _Scitech_Software_Display_Driver_oysney
{
	meta:
		description = "Scitech Software Display Driver"
	strings:
		$a = {56424541462E445256}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
