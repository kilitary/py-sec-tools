rule _Crunch_V5_0__Bitarts_brygvg
{
	meta:
		description = "Crunch V5_0 __ Bitarts"
	strings:
		$a = {0305C01BB8????8CCA03D08CC981C1????51B9????510606B1??518CD3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
