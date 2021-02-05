rule _RAZOR_1911_encruptor_exhnzc
{
	meta:
		description = "RAZOR 1911 encruptor"
	strings:
		$a = {E8????BF????3BFC72??B44CCD21BE????B9????FDF3A5FC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
