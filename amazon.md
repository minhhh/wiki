# AMAZON
* [Installing ec2 tools](http://blog.bottomlessinc.com/2010/12/installing-the-amazon-ec2-command-line-tools-to-launch-persistent-instances/)
* [How to grow the storage](http://blog.edoceo.com/2009/02/amazon-ebs-how-to-grow-storage.html)
* [How to grow the storage](http://aws-musings.com/how-to-expand-your-ebs-volume/)

```
    Note: Depending on the OS, the volume maybe mounted as `/dev/xvda` instead of `/dev/sda` (Ubuntu 11.10).
    You have to resize the new volume right after you created it otherwise the next time it may be mounted as file system root and you won't be able to do resize it.
```

## Create and mount a new EBS volume
* [How to mount an Amazon EBS disk as a drive in Linux (CentOS)](http://www.coderchris.com/linux/how-to-mount-an-amazon-ebs-disk-as-a-drive-in-linux-centos/2011/01/31)

```
    Create a new volume, using the console

    Attach it to the instance, mount point `/dev/sdf`. In ubuntu, it may appear as `/dev/xvdf`

    Format using ext3 or ext 4: `# mkfs.ext3 /dev/sdf`

    Create mount point: `mkdir /media/sdf`

    Add reference to `/etc/fstab`: `#  echo "/dev/xvdf /media/sdf ext3 noatime 0 0" >> /etc/fstab`

    Remount: `mount -a`
```



# AMAZONE DRIVE
* [Experienced Amazon Cloud Drive users - Tips? Useful utilities?](https://www.reddit.com/r/DataHoarder/comments/3uj5v4/experienced_amazon_cloud_drive_users_tips_useful/)
    * [rclone](https://github.com/ncw/rclone)
    * [acd_cli](https://acd-cli.readthedocs.io/en/latest/index.html)
